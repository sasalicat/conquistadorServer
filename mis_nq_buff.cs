using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class mis_nq_buff : Buff
{
    public float jishiqi = 3f;
    public override float Duration
    {
        get
        {
            return 5;
        }
    }


    public override bool onInit(RoleState role, Buff[] Repetitive)
    {
        if (Repetitive == null)
        {
            Debug.Log("onInit Enter Null");
            role.immune_attack = true;
        }
        return true;
    }

    public override void onRemove(RoleState role)
    {

    }
    public override void onIntarvel(RoleState role, float timeBetween)
    {
        
    }
    // Use this for initialization
    void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {

	}
}

