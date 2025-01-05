function setup() {

    var subjects = document.getElementsByClassName('subject-dropdown-item');
    for (var i = 0; i < subjects.length; ++i) {
        var subject = subjects[i];
        subject.onclick = function() {
            var subjectDropdown = document.getElementById('subjectMenuButtonText');
            subjectDropdown.textContent = this.textContent;
            var subjectFormField = document.getElementById('subject');
            subjectFormField.value = this.textContent;
            var bookletTypeButton = document.getElementById('bookletTypeMenuButton');
            if (this.textContent === 'UCAT') {
                var bookletTypeDropdown = document.getElementById('bookletTypeMenuButtonText');
                bookletTypeDropdown.textContent = 'Workbook';
                var bookletTypeFormField = document.getElementById('bookletType');
                bookletTypeFormField.value = 'Workbook';
                bookletTypeButton.disabled = true;
            }
            else {
                bookletTypeButton.disabled = false;
            }
        };
    }

    var bookletTypes = document.getElementsByClassName('booklet-type-dropdown-item');
    for (var i = 0; i < bookletTypes.length; ++i) {
        var bookletType = bookletTypes[i];
        bookletType.onclick = function() {
            var bookletTypeDropdown = document.getElementById('bookletTypeMenuButtonText');
            bookletTypeDropdown.textContent = this.textContent;
            var bookletTypeFormField = document.getElementById('bookletType');
            bookletTypeFormField.value = this.textContent;
        };
    }

    var dateTimeString = document.getElementById('time');

    function dateTime() {
        var date = new Date();
        dateTimeString.textContent = date.toString();
    }

    setInterval(dateTime, 1000);

    for (let i = 1; i < 30; i++) {
        const input = document.getElementById("instruction" + i);
        const label = document.getElementById("label" + i);

        if (input !== null) {
            const handleChange = (e) => {
            e.target.checked
                ? label.classList.add("checked")
                : label.classList.remove("checked");
            }

            input.addEventListener('change', handleChange);
        }
    }

}

function validateForm() {
    var subject = document.getElementById('subject').value;
    var bookletType = document.getElementById('bookletType').value;
    if (subject.length === 0 || bookletType.length === 0) {
        alert("Incorrect Subject or Booklet Type");
        return false;
    }
    else {
        return true;
    }
}