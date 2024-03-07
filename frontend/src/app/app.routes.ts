import { Routes } from '@angular/router';
import { HomeComponent } from './modules/home/home.component';
import { LoginComponent } from './modules/auth/pages/login/login.component';
import { LayoutComponent } from './shared/components/layout/layout.component';
import { TablePageComponent } from './modules/tables/pages/table-page/table-page.component';

export const routes: Routes = [
    {
        path: '',
        component: LoginComponent,
    },
    {
        path: 'app',
        component: LayoutComponent,
        children: [
            {
                path: 'tables',
                component: TablePageComponent,
            },
            {
                path: 'menus',
                component: LayoutComponent,
            },
            {
                path: 'orders',
                component: LayoutComponent,
            }
        ]
    }
];
