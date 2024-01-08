import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import { Zones } from '../models/zones.model';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ZonesService {
  baseUrl='http://localhost:3001/lesZones';
  constructor(private http:HttpClient) { }
  getAll(): Observable<Zones[]>{
    return this.http.get<Zones[]>(`${this.baseUrl}`)
  }
}
