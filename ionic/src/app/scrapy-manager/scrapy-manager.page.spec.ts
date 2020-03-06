import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { ScrapyManagerPage } from './scrapy-manager.page';

describe('ScrapyManagerPage', () => {
  let component: ScrapyManagerPage;
  let fixture: ComponentFixture<ScrapyManagerPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ScrapyManagerPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(ScrapyManagerPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
