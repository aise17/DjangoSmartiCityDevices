import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { CompanysPageRoutingModule } from './companys-routing.module';

import { CompanysPage } from './companys.page';
import { MultiFileUploadComponent } from '../../components/multi-file-upload/multi-file-upload.component';
import { FileUploadModule } from 'ng2-file-upload';
import { TableCompanysComponent } from '../../components/table-companys/table-companys.component';


import { DataTablesModule } from 'angular-datatables';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    CompanysPageRoutingModule,
    FileUploadModule,
    DataTablesModule
  ],
  declarations: [CompanysPage, MultiFileUploadComponent, TableCompanysComponent]
})
export class CompanysPageModule {}
