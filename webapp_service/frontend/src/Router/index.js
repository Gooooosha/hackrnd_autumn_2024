import CodeVerificationPage from "../Pages/CodeVerificationPage";
import RegistrationPage from "../Pages/RegistrationPage";
import SignInPage from "../Pages/SignInPage";

export const RoutesPath = [
    {path: '/registration', component: RegistrationPage, exact: true},
    {path: '/signin', component: SignInPage, exact: true},
    {path: '/signin/code', component: CodeVerificationPage, exact: true}
]

