import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterModule],
  template: `
    <nav>
      <a routerLink="/">Documentos</a> |
      <a routerLink="/new">Novo Documento</a>
    </nav>
    <router-outlet></router-outlet>
  `
})
export class AppComponent {}
