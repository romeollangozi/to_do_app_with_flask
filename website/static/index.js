function deleteNote(noteid){
    fetch('/delete_note', {
        method: 'POST',
        body: JSON.stringify({noteid: noteid})
    }).then((_res) => {
        window.location.href= '/';
    })
}