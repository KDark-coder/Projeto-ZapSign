import { Routes } from '@angular/router';
import { DocumentListComponent } from './document-list.component';
import { DocumentFormComponent } from './document-form.component';

export const routes: Routes = [
  { path: '', component: DocumentListComponent },
  { path: 'new', component: DocumentFormComponent },
  { path: '**', redirectTo: '' }
];