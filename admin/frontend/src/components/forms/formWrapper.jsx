import React, { useState } from 'react';
import { useFormik } from 'formik';
import { Form, Button, Input, Panel } from 'rsuite';


export default function Field ({onSubmit, children, ...rest }) {

    return (
        <Form onSubmit={onSubmit}>
            {children}
            
            <Button block appearance="primary" color='green' type="submit">
                Войти
            </Button>
        </Form>
    );
  };

