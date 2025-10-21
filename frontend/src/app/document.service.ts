import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class DocumentService {
  private base = '/api/documents/';
  constructor(private http: HttpClient) {}

  list(): Observable<any> { return this.http.get(this.base); }
  create(payload: any): Observable<any> { return this.http.post(this.base, payload); }
  analyze(id: number): Observable<any> { return this.http.post(`${this.base}${id}/analyze/`, {}); }
}