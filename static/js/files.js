function filesz() {
    const fi = document.getElementById('file');
        if (fi.files.length > 0) {
            for (let n = 0; n <= fi.files.length - 1; n++) {
                const fsize = fi.files.item(n).size;
                const file = Math.round((fsize / 1024));
                    if (file >= 20000) {
                    alert("File too Big, please select a file less than 20mb");
                    } else{
                    document.getElementById('size').innerHTML = '<b>'
                        + file + '</b> KB';
                        let txt  = document.getElementById('size');
                        txt.style.textAlign="center";
                }
            }
        }
    }