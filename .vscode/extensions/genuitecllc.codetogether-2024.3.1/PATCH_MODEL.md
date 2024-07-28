Extension Host         Render Process

editor.document        Editor Buffer
   seq no                  seq no

ctDocs                 
   mirror of edit.doc


- When we have incoming changes, we calculate against ctDoc the edit to apply
- We then try to use the editor if activeEditor == uri, and apply change
- If editor used, the change is sent with a seq no
  
# Incoming Edit

1. Calculate patch against ctDoc
2. Apply against editor.edit(...)
3. In parallel, if Render process has a user typing, the render's seq no can change
4. Render seq always wins, causing rejection of incoming patch
5. We then retry recalculating against against a 'consistent' ctDoc and try again



*IMPORTANT*
Make sure we block the apply of remote patch
until the didChangeTextDocument has been received