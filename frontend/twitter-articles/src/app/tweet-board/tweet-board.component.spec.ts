import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TweetBoardComponent } from './tweet-board.component';

describe('TweetBoardComponent', () => {
  let component: TweetBoardComponent;
  let fixture: ComponentFixture<TweetBoardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TweetBoardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TweetBoardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
