import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrendsBoardComponent } from './trends-board.component';

describe('TrendsBoardComponent', () => {
  let component: TrendsBoardComponent;
  let fixture: ComponentFixture<TrendsBoardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrendsBoardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrendsBoardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
