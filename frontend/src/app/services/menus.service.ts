import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { CustomResponse } from '../shared/models/menu.model';

@Injectable({
  providedIn: 'root'
})
export class MenusService {

  private http = inject(HttpClient)

  constructor() { }

  getMenus() {
    const httpOptions = {
      headers: new HttpHeaders({
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXJAdGVzdC5jb20iLCJleHAiOjE3MDk4MTI4MTV9.RjSoQl-Nq0LWu3nC_Xk0gv3FLmjBcyscnmQv4IrYo6E'
      })
    };
    return this.http.get<CustomResponse>('http://localhost:8000/menus', httpOptions)
  }
}
