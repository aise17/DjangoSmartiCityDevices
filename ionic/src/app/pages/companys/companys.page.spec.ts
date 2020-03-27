import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { CompanysPage } from './companys.page';

describe('CompanysPage', () => {
  let component: CompanysPage;
  let fixture: ComponentFixture<CompanysPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CompanysPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(CompanysPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
