export const useIsNewTaskVisible = () =>
  useState<boolean>("isNewTaskVisible", () => false);
