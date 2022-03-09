import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CountsDBComponent } from './counts-db.component';

describe('CountsDBComponent', () => {
  let component: CountsDBComponent;
  let fixture: ComponentFixture<CountsDBComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CountsDBComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CountsDBComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
