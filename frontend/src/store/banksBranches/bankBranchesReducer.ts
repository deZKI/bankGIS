import {initialState} from "../reducer";
import {SET_BANK_BRANCHES, SetBankBranchesAction} from "./bankBranchesActions";
import {IBankBranch} from "../../hooks/useBanksBranchesData";

export interface IBranchBranchesState {
  branchBranches: IBankBranch[];
}

type BankBranchesActions = SetBankBranchesAction;

export const bankBranchesReducer = (state = initialState.bankBranches, action: BankBranchesActions): IBranchBranchesState => {
  switch (action.type) {
    case SET_BANK_BRANCHES:
      return {
        ...state,
        branchBranches: action.bankBranches
      }
    default:
      return state;
  }
}
