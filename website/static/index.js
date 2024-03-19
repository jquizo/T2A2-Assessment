// Function for deleting notes

function deleteNote(noteId) {
    // Passes the noteId to the endpoint  
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      // After response, reload window
      window.location.href = "/";
    });
  }
  