export const useIsNewTaskVisible = () =>
  useState<boolean>("isNewTaskVisible", () => false);

export const useIsDetailTaskVisible = () =>
  useState<boolean>("isDetailTaskVisible", () => true);
