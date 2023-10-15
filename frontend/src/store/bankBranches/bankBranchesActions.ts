import { Action, ActionCreator } from "redux";
import { ThunkAction } from "redux-thunk";
import { IInitialState } from "../reducer";
import {IBankBranch} from "../../hooks/useBankBranchesData";
import axios from "axios";

export const SET_BANK_BRANCHES = 'SET_BANK_BRANCHES';

export type SetBankBranchesAction = {
  type: typeof SET_BANK_BRANCHES;
  bankBranches: IBankBranch[];
}

export const setBankBranches: ActionCreator<SetBankBranchesAction> = (bankBranches) => ({
  type: SET_BANK_BRANCHES,
  bankBranches
})

export const setBankBranchesAsync = (): ThunkAction<void, IInitialState, unknown, Action<string>> => (dispatch) => {
  fetch('http://localhost:8000/api/bank-branches/?latitude=37.6156&longitude=55.7522')
    .then((res) => {
      const bankBranches = res;
      console.log(bankBranches);
      // dispatch(setBankBranches(bankBranches));
    })
    .catch((error) => {
      console.log(error);
    })
}