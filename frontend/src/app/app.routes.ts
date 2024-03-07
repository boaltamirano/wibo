import { Routes } from '@angular/router';
import { HomeComponent } from './modules/home/home.component';
import { LoginComponent } from './modules/auth/pages/login/login.component';

export const routes: Routes = [
    {
        path: 'login',
        component: LoginComponent,
    }
];
