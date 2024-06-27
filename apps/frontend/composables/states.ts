export const useIsNewTaskVisible = () =>
  useState<boolean>("isNewTaskVisible", () => false);

export const useIsDetailTaskVisible = () =>
  useState<boolean>(`isDetailTaskVisible`, () => false);

export const useTaskId = () => useState<number>(`taskId`, () => -1);
