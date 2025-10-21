import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <nav>
      <a routerLink="/">Documentos</a> |
      <a routerLink="/new">Novo Documento</a>
    </nav>
    <router-outlet></router-outlet>
  `
})
export class AppComponent {}