import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ScrapyManagerPageRoutingModule } from './scrapy-manager-routing.module';

import { ScrapyManagerPage } from './scrapy-manager.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ScrapyManagerPageRoutingModule
  ],
  declarations: [ScrapyManagerPage]
})
export class ScrapyManagerPageModule {}
