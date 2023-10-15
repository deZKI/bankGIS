import {useEffect} from "react";
import {useDispatch, useSelector} from "react-redux";
import {IInitialState} from "../store/reducer";
import {setBankBranchesAsync} from "../store/banksBranches/bankBranchesActions";
import {ThunkDispatch} from "redux-thunk";
import {AnyAction} from "redux";

export interface IOpenHours {
  days: string;
  hours: string;
}

export interface IOpenHoursIndividual {
  days: string;
  hours: string;
}

export interface IBankBranch {
  address: string;
  open_hours: IOpenHours[];
  open_hours_individual: IOpenHoursIndividual[];
  lat: string;
  lon: string;
}

export function useBanksBranchesData() {
  const bankBranches = useSelector<IInitialState, IBankBranch[]>(state => state.bankBranches.branchBranches);
  const dispatch = useDispatch<ThunkDispatch<IInitialState, void, AnyAction>>();

  useEffect(() => {
    dispatch(setBankBranchesAsync());
  }, []);

  return bankBranches;
}
