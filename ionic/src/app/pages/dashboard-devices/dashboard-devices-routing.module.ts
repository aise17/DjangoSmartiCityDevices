import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DashboardDevicesPage } from './dashboard-devices.page';

const routes: Routes = [
  {
    path: '',
    component: DashboardDevicesPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DashboardDevicesPageRoutingModule {}
