import { Component, OnInit } from '@angular/core';
import { DocumentService } from './document.service';

@Component({
  selector: 'app-document-list',
  template: `
    <h2>Documentos</h2>
    <div *ngIf="loading">Carregando...</div>
    <ul>
      <li *ngFor="let d of documents">{{d.name}} - {{d.status}}</li>
    </ul>
  `
})
export class DocumentListComponent implements OnInit {
  documents: any[] = [];
  loading = false;
  constructor(private svc: DocumentService) {}
  ngOnInit(){ this.loading = true; this.svc.list().subscribe(r=>{ this.documents = r; this.loading = false; }, ()=> this.loading = false); }
}