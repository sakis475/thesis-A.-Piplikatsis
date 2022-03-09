import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ArticlesBoardComponent } from './articles-board.component';

describe('ArticlesBoardComponent', () => {
  let component: ArticlesBoardComponent;
  let fixture: ComponentFixture<ArticlesBoardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ArticlesBoardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ArticlesBoardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
