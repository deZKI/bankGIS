import {initialState} from "../reducer";
import {SET_BANK_BRANCHES, SetBankBranchesAction} from "./bankBranchesActions";
import {IBankBranch} from "../../hooks/useBankBranchesData";

export interface IBankBranchesState {
  bankBranches: IBankBranch[];
}

type BankBranchesActions = SetBankBranchesAction;

export const bankBranchesReducer = (state = initialState.bankBranches, action: BankBranchesActions): IBankBranchesState => {
  switch (action.type) {
    case SET_BANK_BRANCHES:
      return {
        ...state,
        bankBranches: action.bankBranches
      }
    default:
      return state;
  }
}
