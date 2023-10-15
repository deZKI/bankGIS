import {Action, ActionCreator} from "redux";
import {ThunkAction} from "redux-thunk";
import {IInitialState} from "../reducer";
import {IBankBranch} from "../../hooks/useBanksBranchesData";
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
  axios.get('/api/bank-branches', {
    headers: {}
  })
    .then((res) => {
      const bankBranches = res;
      console.log(bankBranches);
      // dispatch(setTransactions(transactions));
    })
    .catch((error) => {
      console.log(error);
    })
}
