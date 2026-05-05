import { describe, expect, it } from 'vitest';

import { answerCookingQuestion } from './assistant';
import { getJitsiUrl, getLessonById, lessons } from './culinary-data';

describe('Culinária Live data and assistant', () => {
  it('provides scheduled live cooking lessons with recipe steps', () => {
    expect(lessons.length).toBeGreaterThanOrEqual(3);
    expect(lessons[0].chef).toContain('Chef');
    expect(lessons[0].steps.length).toBeGreaterThan(3);
    expect(lessons[0].ingredients.length).toBeGreaterThan(5);
  });

  it('creates a valid Jitsi Meet URL for a live class room', () => {
    const lesson = getLessonById('moqueca-baiana');
    const url = getJitsiUrl(lesson.jitsiRoom);
    expect(url).toContain('https://meet.jit.si/');
    expect(url).toContain('CulinariaLiveMoquecaBaianaNoiteCorrida');
    expect(url).toContain('prejoinPageEnabled=false');
  });

  it('answers recipe-specific substitution questions', () => {
    const answer = answerCookingQuestion('Posso substituir algum ingrediente?', 'moqueca-baiana');
    expect(answer.toLowerCase()).toContain('moqueca');
    expect(answer).toContain('substituições');
  });

  it('answers voice-style next step commands with contextual guidance', () => {
    const answer = answerCookingQuestion('Próximo passo', 'moqueca-baiana');
    expect(answer).toContain('Próximo passo');
    expect(answer).toContain('bancada');
  });
});
