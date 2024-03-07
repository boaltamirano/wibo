import { Routes } from '@angular/router';
import { LoginComponent } from './modules/auth/pages/login/login.component';
import { LayoutComponent } from './shared/components/layout/layout.component';
import { TablePageComponent } from './modules/tables/pages/table-page/table-page.component';
import { MenusPageComponent } from './modules/menus/pages/menus-page/menus-page.component';
import { OrderComponent } from './modules/orders/components/order/order.component';
import { loginGuard } from './guards/login.guards';

export const routes: Routes = [
    {
        path: 'login',
        component: LoginComponent,
    },
    {
        path: '',
        component: LoginComponent,
    },
    {
        path: 'app',
        component: LayoutComponent,
        canActivate: [loginGuard],
        children: [
            {
                path: 'tables',
                component: TablePageComponent,
            },
            {
                path: 'menus',
                component: MenusPageComponent,
            },
            {
                path: 'orders',
                component: OrderComponent,
            }
        ]
    },
    {
        path: '**',
        redirectTo: 'login',
    },
];
