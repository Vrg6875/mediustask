/* TODOS
- [ ] fix dragging in the opposite direction
*/

chrome.runtime.onInstalled.addListener(() => {
  // console.log("INSTALLED");
});

chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: activeCopyAndPasteVideo,
  });
});

// chrome.commands.onCommand.addListener((command) => {
//   console.log(command);
//   if (command === "get_current_tab") {
//     chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
//       const tab = tabs[0];
//       // console.log("Current tab ID:", tab.id);
//       // console.log("Current tab URL:", tab.url);
//       // console.log("Current tab title:", tab.title);
//     });
//   }
// });

function activeCopyAndPasteVideo() {
  const $ = {
    video: document.querySelector("video"),
    isInitialized: !!document.querySelector("#cpv-highlight"),
    highlight:
      document.querySelector("#cpv-highlight") || document.createElement("div"),
    ocr_canvas:
      document.querySelector("#cpv-canvas") || document.createElement("canvas"),
    copypaste:
      document.querySelector("#cpv-copypaste") || document.createElement("div"),
    loading:
      document.querySelector("#cpv-loading") || document.createElement("div"),
    toast:
      document.querySelector("#cpv-toast") || document.createElement("div"),
  };

  const App = {
    isDragging: false,
    init() {
      if (!$.video) return;
      if (!$.isInitialized) App.setup();
      // indicate that they can start selecting text from the video
      document.body.style.cursor = "crosshair";
      $.copypaste.style.display = "block";
      $.video.pause();
    },
    setup() {
      $.highlight.setAttribute("id", "cpv-highlight");
      $.highlight.style.position = "absolute";
      $.highlight.style.pointerEvents = "none";
      $.highlight.style.zIndex = "99";
      document.body.appendChild($.highlight);

      $.ocr_canvas.setAttribute("id", "cpv-canvas");
      document.body.appendChild($.ocr_canvas);

      $.copypaste.setAttribute("id", "cpv-copypaste");
      document.body.appendChild($.copypaste);

      $.loading.setAttribute("id", "cpv-loading");
      $.loading.innerHTML = `<div id="cpv-loading-inner"><div></div><div></div></div>`;
      document.body.appendChild($.loading);

      $.toast.setAttribute("id", "cpv-toast");
      document.body.appendChild($.toast);

      document.addEventListener("keydown", (event) => {
        if (event.key == "Escape") App.end();
      });
      $.copypaste.addEventListener("mousedown", App.onDragStart);
      $.copypaste.addEventListener("mousemove", App.onDrag);
      $.copypaste.addEventListener("mouseup", App.onDragEnd);
    },
    end() {
      App.hideLoading();
      document.body.style.cursor = "default";
      // reset the highlight box for next time
      $.copypaste.style.display = "none";
      $.highlight.style.top = "0";
      $.highlight.style.left = "0";
      $.highlight.style.width = "0";
      $.highlight.style.height = "0";
      $.highlight.style.display = "none";
      $.highlight.style.background = "none";
      $.highlight.style.boxShadow = "none";
    },
    showToast(message, duration = 3000) {
      $.toast.textContent = message;
      $.toast.classList.add("show");

      setTimeout(() => {
        $.toast.classList.remove("show");
      }, duration);
    },
    showLoading() {
      $.loading.style.display = "block";
      const rect = $.highlight.getBoundingClientRect();
      const top = parseInt($.highlight.style.top, 10) + rect.height / 2 - 75;
      const left = parseInt($.highlight.style.left, 10) + rect.width / 2 - 75;
      // console.log(rect, top, left);
      $.loading.style.top = `${top}px`;
      $.loading.style.left = `${left}px`;
    },
    hideLoading() {
      $.loading.style.display = "none";
    },
    copyToClipboard(text) {
      return new Promise((resolve, reject) => {
        navigator.clipboard
          .writeText(text)
          .then(() => {
            // console.log(`Copied! ${text}`);
            resolve(text);
          })
          .catch((error) => {
            // console.log(`Copy failed! ${error}`);
            reject();
          });
      });
    },
    onDragStart(e) {
      App.isDragging = true;

      $.highlight.dataset.startx = e.pageX;
      $.highlight.dataset.starty = e.pageY;
      $.highlight.style.display = "block";
      $.highlight.style.border = "3px dotted black";
      // $.highlight.style.boxShadow = "0 2px 5px rgb(255 255 255 / 0.6)";
      $.highlight.style.background = "rgba(255, 255, 255, 0.2)";
      $.highlight.style.opacity = 1;
      $.highlight.style.left = `${e.pageX}px`;
      $.highlight.style.top = `${e.pageY}px`;
    },
    onDrag(e) {
      if (App.isDragging) {
        requestAnimationFrame(function () {
          $.highlight.style.width = `${e.pageX - $.highlight.dataset.startx}px`;
          $.highlight.style.height = `${
            e.pageY - $.highlight.dataset.starty
          }px`;
        });
      }
    },
    onDragEnd(e) {
      App.isDragging = false;
      App.showLoading();
      App.drawOCRCanvas();
    },
    drawOCRCanvas() {
      const rect = $.highlight.getBoundingClientRect();
      const videoRect = $.video.getBoundingClientRect();

      let top = rect.y - videoRect.y;
      let left = rect.x - videoRect.x;
      let width = rect.width;
      let height = rect.height;

      // ignore if the selection is too small
      if (width < 10 || height < 10) {
        App.end();
        return;
      }

      // lets say the video is 3840x2160 (4k)
      const aspectRatio = $.video.videoWidth / $.video.videoHeight;

      // but the video element is too wide, 1528x570
      // a black bar is on the left and right
      // the actual video is 1.7777777777777777 times the height of the video element
      const videoElementAspectRatio =
        $.video.offsetWidth / $.video.offsetHeight;
      let blackbarSize = 0;
      let scale = 1;
      // console.log(
      //   "videoElementAspectRatio",
      //   videoElementAspectRatio,
      //   left,
      //   top
      // );

      // console.log(
      //   `BEFORE top: ${top}, left: ${left}, width: ${width}, height: ${height}`
      // );

      if (videoElementAspectRatio > aspectRatio) {
        // there is a black bar on the left and right
        const videoHeight = $.video.offsetHeight;
        const videoWidth = videoHeight * aspectRatio;
        blackbarSize = ($.video.offsetWidth - videoWidth) / 2;
        left = Math.floor(left - blackbarSize);
        // the problem with finding where to draw
        // is the video is smaller than the actual dimensions of the video
        // so we need to scale the coordinates

        // the video element is 1528x570
        // the video is 3840x2160
        // so we need to scale the coordinates by 3.789473684210526
        scale = $.video.videoHeight / $.video.offsetHeight;
      }
      if (videoElementAspectRatio < aspectRatio) {
        // there is a black bar on the top and bottom
        const videoWidth = $.video.offsetWidth;
        const videoHeight = videoWidth / aspectRatio;
        blackbarSize = ($.video.offsetHeight - videoHeight) / 2;
        top = Math.floor(top - blackbarSize);
        scale = $.video.videoWidth / $.video.offsetWidth;
      }

      // console.log(
      //   `AFTER top: ${top}, left: ${left}, width: ${width}, height: ${height}`
      // );

      top = Math.floor(top * scale);
      left = Math.floor(left * scale);
      width = Math.floor(width * scale);
      height = Math.floor(height * scale);

      // console.log(`top: ${top} left: ${left} width: ${width} height: ${height}`);

      // the canvas needs to be the same size as the video
      // so we need to scale the canvas
      $.ocr_canvas.width = width;
      $.ocr_canvas.height = height;
      $.ocr_canvas
        .getContext("2d")
        .drawImage($.video, left, top, width, height, 0, 0, width, height);

      App.preprocessImage();
    },
    async preprocessImage() {
      // debug what it's capturing
      // Debug.on();

      // Write the blob to an image tag
      const image = await imageFromCanvas($.ocr_canvas);

      try {
        const result = await Tesseract.recognize(image, "eng");
        // console.log("Tesseract result:", result);
        const copiedText = await App.copyToClipboard(result.data.text);

        // App.showToast(`Copied: ${copiedText}`);
        App.showToast(`ClipWords copied the text into your clipboard!`);

        // pop up a toast message to indicate that the text has been copied

        App.end();
        // Debug.off();
      } catch (error) {
        App.end();
        // Debug.off(0);
      }
    },
  };

  async function imageFromCanvas(canvas) {
    return new Promise((resolve, reject) => {
      canvas.toBlob((blob) => {
        const newImg = document.createElement("img");
        const url = URL.createObjectURL(blob);

        newImg.onload = () => {
          // no longer need to read the blob so it's revoked
          URL.revokeObjectURL(url);
        };

        resolve(url);
      });
    });
  }

  const Debug = {
    on() {
      $.ocr_canvas.style.position = "absolute";
      $.ocr_canvas.style.top = 0;
      $.ocr_canvas.style.left = 0;
      $.ocr_canvas.style.display = "block";
      $.ocr_canvas.style.zIndex = 99999;
    },
    off(delay = 1000) {
      setTimeout(function () {
        $.ocr_canvas.style.display = "none";
      }, delay);
    },
  };

  App.init();
}
