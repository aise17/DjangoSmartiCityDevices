import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { DashboardDevicesPageRoutingModule } from './dashboard-devices-routing.module';

import { DashboardDevicesPage } from './dashboard-devices.page';

import { DataTablesModule } from 'angular-datatables';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    DashboardDevicesPageRoutingModule,
    DataTablesModule
  ],
  declarations: [DashboardDevicesPage]
})
export class DashboardDevicesPageModule {}
