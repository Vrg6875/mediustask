function filterCanvas(canvas, filter, amount) {
  const { width, height } = canvas;
  const ctx = canvas.getContext("2d");
  var text2image = new Konva.Image({
    x: 0,
    y: 0,
    image: canvas,
    width,
    height,
  });

  text2image.cache();

  switch (filter) {
    case "enhance": {
      text2image.filters([Konva.Filters.Enhance]);
      text2image.enhance(amount);
      break;
    }
    case "grayscale": {
      text2image.filters([Konva.Filters.Grayscale]);
      break;
    }
    case "brightness": {
      text2image.filters([Konva.Filters.Brighten]);
      text2image.brightness(amount);
      break;
    }
    case "contrast": {
      text2image.filters([Konva.Filters.Contrast]);
      text2image.contrast(amount);
      break;
    }
  }

  const export_canvas = text2image.toCanvas({ width, height });
  const export_ctx = export_canvas.getContext("2d");
  const exportData = export_ctx.getImageData(0, 0, width, height);

  ctx.putImageData(exportData, 0, 0);
}

function binarizeCanvas(canvas) {
  const ctx = canvas.getContext("2d");
  const threshold = 100;
  const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
  const data = imageData.data;

  for (let i = 0; i < data.length; i += 4) {
    // Calculate the grayscale value
    const grayscale =
      0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2];

    // Apply the threshold
    const binary = grayscale > threshold ? 255 : 0;

    // Update the pixel values
    data[i] = data[i + 1] = data[i + 2] = binary;
  }

  ctx.putImageData(imageData, 0, 0);
  return imageData;
}
