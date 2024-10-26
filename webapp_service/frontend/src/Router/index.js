import CodeVerificationPage from "../Pages/CodeVerificationPage";
import HomePage from "../Pages/HomePage";
import RegistrationPage from "../Pages/RegistrationPage";
import SignInPage from "../Pages/SignInPage";

export const RoutesPath = [
    {path: '/', component: HomePage, exact: true},
    {path: '/registration', component: RegistrationPage, exact: true},
    {path: '/signin', component: SignInPage, exact: true},
    {path: '/signin/code', component: CodeVerificationPage, exact: true}
]

