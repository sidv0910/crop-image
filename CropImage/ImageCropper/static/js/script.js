function setup() {
    document.getElementById('submit-button').addEventListener('click', openDialog);

    function openDialog() {
        document.getElementById('formFile').click();
    }

    document.getElementById('formFile').addEventListener('change', submitForm);

    function submitForm() {
        if (validateForm()) {
            updateDisplay();
            document.getElementById('upload-form').submit();
        }
        else {
            window.location.href = "";
        }
    }

    function updateDisplay() {
        document.getElementById('upload-form').style.display = 'none';
        document.getElementById('spinner-border').style.display = 'inline-block';
    }

    function validateForm() {
        var fileList = document.getElementById("formFile").files;
        var extension = fileList[0].type;
        if (!(extension === "image/png" || extension === "image/jpeg" || extension === "image/jpg" || extension === "application/zip")) {
            alert("Invalid file format");
            return false;
        }
        if (extension === "application/zip" && fileList.length > 1) {
            alert("Only single zip file is allowed");
            return false;
        }
        for (var i = 0; i < fileList.length; i++) {
            if (fileList[i].type != extension) {
                alert("Please select files of same type");
                return false;
            }
        }
        return true;
    }
}