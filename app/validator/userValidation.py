from cerberus import Validator

userSignUpValidation = Validator({ 
    'email': { 'type': 'string' },
    'password': { 'type': 'string' }
})