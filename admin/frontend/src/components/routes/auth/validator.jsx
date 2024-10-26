export default function validator(values) {
  const errors = {};

  if (!values.login) {
    errors.login = 'Заполните поле';
  }
  if (!values.password) {
    errors.password = 'Заполните поле';
  }

  return errors;
};