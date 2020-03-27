import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CompanysPage } from './companys.page';

const routes: Routes = [
  {
    path: '',
    component: CompanysPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class CompanysPageRoutingModule {}
