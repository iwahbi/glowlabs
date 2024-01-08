import { Component, OnInit } from '@angular/core';
import { Zones } from 'src/app/models/zones.model';
import { ZonesService } from 'src/app/services/zones.service';

@Component({
  selector: 'app-zones',
  templateUrl: './zones.component.html',
  styleUrls: ['./zones.component.css']
})
export class ZonesComponent implements OnInit {
  myzones:Zones[] |undefined;
  constructor(private ZonesService:ZonesService) { }

  ngOnInit(): void {


    this.recZones();
    //this is to call recZones after every 1000 seconds
    setInterval(this.recZones,1000)

  }

  recZones(){
    this.ZonesService.getAll.subscribe({
      next:(data)=>this.myzones=(data),
      error:(e)=>console.error(e),
      complete:()=>console.log('bingo...get done')

    })
  }
}
