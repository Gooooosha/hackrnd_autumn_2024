import React, { useState } from "react";
import RegistrationForm from "../components/RegistrationForm";
import MyModal from "../components/MyModal/MyModal";

const RegistrationPage = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <>
      <RegistrationForm setModal={setIsModalOpen} />
      {isModalOpen && <MyModal setVisible={setIsModalOpen} visible={isModalOpen}>Форма отправлена успешно!</MyModal>}
    </>
  );
};

export default RegistrationPage;