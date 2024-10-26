import React, { createContext, useContext, useState, useEffect } from 'react';
import { getCookie } from '../../utils/CookieManager';
import { get_role_by_token } from '../../api/auth';

const RoleContext = createContext();

export const RoleProvider = ({ children }) => {
  const [role, setRole] = useState(null);

  useEffect(() => {
    const fetchRole = async () => {
      const token = getCookie('token');
      if (token) {
        // const role = await get_role_by_token({ token });
        const role = 'admin';
        if (role) {
          setRole(role);
        }
      } else {
        setRole(null);
      }
    };

    fetchRole();
  }, []);

  return (
    <RoleContext.Provider value={{ role, setRole }}>
      {children}
    </RoleContext.Provider>
  );
};

export const useRole = () => {
  return useContext(RoleContext);
};
