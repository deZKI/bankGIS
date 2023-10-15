import {useDispatch, useSelector} from "react-redux";
import {IInitialState} from "../store/reducer";
import {ThunkDispatch} from "redux-thunk";
import {AnyAction} from "redux";
import {useEffect} from "react";
import {setBankBranchesAsync} from "../store/bankBranches/bankBranchesActions";

export interface IOpenHour {
  days: string;
  hours: string;
}

export interface IOpenHourIndividual {
  days: string;
  hours: string;
}

export interface IBankBranch {
  address: string;
  open_hours: IOpenHour[];
  open_hours_individual: IOpenHourIndividual[];
  lat: string;
  lon: string;
}

export function useBankBranchesData() {
  const bankBranches = useSelector<IInitialState, IBankBranch[]>(state => state.bankBranches.bankBranches);
  const dispatch = useDispatch<ThunkDispatch<IInitialState, void, AnyAction>>();

  useEffect(() => {
    dispatch(setBankBranchesAsync());
  }, []);

  return bankBranches;
}
