import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { DocumentService } from './document.service';

@Component({
  selector: 'app-document-form',
  template: `
    <h2>Novo Documento</h2>
    <form (ngSubmit)="submit()">
      <label>Nome: <input [(ngModel)]="name" name="name"></label><br>
      <label>File URL: <input [(ngModel)]="file_url" name="file_url"></label><br>
      <label>Signer Name: <input [(ngModel)]="signer_name" name="signer_name"></label><br>
      <label>Signer Email: <input [(ngModel)]="signer_email" name="signer_email"></label><br>
      <button type="submit">Enviar</button>
    </form>
  `
})
export class DocumentFormComponent {
  name = '';
  file_url = '';
  signer_name = '';
  signer_email = '';
  constructor(private svc: DocumentService, private router: Router) {}
  submit(){
    const payload = { name: this.name, file_url: this.file_url, signers: [{ name: this.signer_name, email: this.signer_email }] };
    this.svc.create(payload).subscribe(()=> this.router.navigate(['/']));
  }
}