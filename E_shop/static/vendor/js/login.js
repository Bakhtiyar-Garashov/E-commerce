const frmSignIn = document.getElementById('frmSignIn');
const frmForget = document.getElementById('frmForget');
const frmRegister = document.getElementById('frmRegister');

const inputs = document.querySelectorAll('.asm-form__input');
const showPasswordTogglers = document.querySelectorAll('[data-action="toggle-show-password"]');
const linkButtons = document.querySelectorAll('[data-action="show-form"]');

/* Functions */
const inputLabelFocusOut = event => {
    label = document.querySelector(`label[for="${event.target.id}"]`);
    if (event.target.value.length > 0) {
        label.classList.add('active');
        label.parentNode.classList.remove('invalid');
    } else {
        label.classList.remove('active');
    }
}

const inputLabelFocus = event => {
    label = document.querySelector(`label[for="${event.target.id}"]`);
    label.classList.add('active');
    label.parentNode.classList.remove('invalid');
}

const toggleShowPassword = event => {
    const input = document.querySelector(event.target.dataset.input);
    const type = input.getAttribute('type');
    input.setAttribute('type', type === 'password' ? 'text' : 'password');
}

const showForm = event => {
    event.preventDefault();

    for (const form of document.querySelectorAll('.asm-form')) {
        form.classList.remove('active');
    }

    for (const error of document.querySelectorAll('.asm-form__inputbox.invalid')) {
        error.classList.remove('invalid');
    }

    document.querySelector(event.target.dataset.target).classList.add('active');
}

/* Listener assigns */

for (const input of inputs) {
    input.addEventListener('focusout', inputLabelFocusOut);
    input.addEventListener('focus', inputLabelFocus);
}

for (const toggler of showPasswordTogglers) {
    toggler.addEventListener('click', toggleShowPassword);
}

for (const button of linkButtons) {
    button.addEventListener('click', showForm);
}

/* Form Validator*/

const validateForm = form => {
    const inputs = form.querySelectorAll('.validate');
    for (const input of inputs) {

        input.classList.remove('invalid');
        input.parentNode.classList.remove('invalid');

        let allOK = true;

        switch (input.dataset.validation) {
            case 'regex':
                {
                    allOK = input.value.match(new RegExp(input.dataset.regex));
                    break;
                }
            case 'match':
                {
                    allOK = input.value === form.querySelector(input.dataset.target).value;
                    break;
                }
            default:
                {
                    allOK = false;
                    break;
                }
        } //end of switch

        if (!allOK) {
            input.classList.add('invalid');
            input.parentNode.classList.add('invalid');
            return false;
        }
    } //end of for-of

}