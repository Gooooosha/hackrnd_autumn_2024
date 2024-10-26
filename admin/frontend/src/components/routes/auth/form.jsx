import React from 'react';
import { useFormik } from 'formik';
import Field from '../../forms/formField';
import FormWrapper from '../../forms/formWrapper';
import validator from './validator';
import { createSearchParams, useNavigate } from 'react-router-dom';
import { useSearchParams, useLocation } from 'react-router-dom';
import { login, get_role_by_token } from '../../../api/auth';
import { setCookie } from '../../../utils/CookieManager';
import { useRole } from '../RoleContext';

export default function Auth() {
  const { state } = useLocation();
  const { _login, password } = state || {};
  const navigator = useNavigate();
  const { setRole } = useRole();

  const formik = useFormik({
    initialValues: {
      login: _login || '',
      password: password || '',
    },
    validate: validator,
    onSubmit: async values => {
      try {
          // const response = await login(values);
          const response = {
              token: 'token'
          };
          if (response.token) {
            setCookie('token', response.token, { expires: 1000000, path: '/' });
            // const role_response = await get_role_by_token({ token: response.token});
            const role_response = {
                role: 'admin'
            };

            setRole(role_response.role);

            navigator('/database');

          }
          
      } catch (error) {
          console.error("Login error:", error.message);
      }
  }
  });

  return (
    <FormWrapper onSubmit={formik.handleSubmit}>
      <Field
        name="login"
        placeholder={'Логин'}
        label={'Логин'}
        value={formik.values.login}
        error={formik.errors.login}
        onChange={value => formik.setFieldValue('login', value)}
      />
      <Field
        name="password"
        placeholder={'Пароль'}
        label={'Пароль'}
        type="password"
        value={formik.values.password}
        error={formik.errors.password}
        onChange={value => formik.setFieldValue('password', value)}
      />
    </FormWrapper>
  );
}
