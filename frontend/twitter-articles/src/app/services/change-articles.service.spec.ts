import { TestBed } from '@angular/core/testing';

import { ChangeArticlesService } from './change-articles.service';

describe('ChangeArticlesService', () => {
  let service: ChangeArticlesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ChangeArticlesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
