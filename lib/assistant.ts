import { getLessonById, profile } from './culinary-data';

const normalize = (value: string) => value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');

export function answerCookingQuestion(question: string, lessonId = 'moqueca-baiana') {
  const lesson = getLessonById(lessonId);
  const text = normalize(question);

  if (text.includes('substituir') || text.includes('trocar')) {
    return `Para a receita ${lesson.title}, faça substituições mantendo a função do ingrediente. Se faltar leite de coco, use creme vegetal leve com um pouco de água; se faltar coentro, use salsinha, sabendo que o sabor ficará mais suave.`;
  }

  if (text.includes('tempo') || text.includes('quanto falta')) {
    return `Nesta aula, acompanhe o tempo pelo passo atual. A etapa mais sensível é o cozimento principal: mantenha fogo médio e observe textura, aroma e ponto, em vez de depender apenas do relógio.`;
  }

  if (text.includes('proximo') || text.includes('próximo')) {
    return `Próximo passo: ${lesson.steps[1] ?? lesson.steps[0]}. Antes de avançar, confirme que sua bancada está organizada e que os ingredientes principais estão ao alcance.`;
  }

  if (text.includes('ponto') || text.includes('cozimento')) {
    return `O ponto ideal aparece quando a textura muda sem ressecar. No seu perfil ${profile.level}, recomendo observar cor, firmeza e aroma, e reduzir o fogo se a panela estiver borbulhando demais.`;
  }

  return `Pensando na receita ${lesson.title}, minha orientação é seguir a ordem da chef, separar ingredientes antes de cozinhar e perguntar sempre que uma etapa parecer rápida demais. Dica contextual: ${lesson.tips[0]}`;
}

export const quickQuestions = [
  'Qual é o próximo passo?',
  'Posso substituir algum ingrediente?',
  'Como sei o ponto correto?',
  'Quanto tempo falta?',
];

export const voiceCommands = [
  'Próximo passo',
  'Repetir ingredientes',
  'Quanto tempo falta?',
  'Posso substituir manteiga?',
];
