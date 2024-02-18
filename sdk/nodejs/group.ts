// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class Group extends pulumi.CustomResource {
    /**
     * Get an existing Group resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState, opts?: pulumi.CustomResourceOptions): Group {
        return new Group(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cpln:index/group:Group';

    /**
     * Returns true if the given object is an instance of Group.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Group {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Group.__pulumiType;
    }

    public /*out*/ readonly cplnId!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly identityMatcher!: pulumi.Output<outputs.GroupIdentityMatcher | undefined>;
    public readonly memberQuery!: pulumi.Output<outputs.GroupMemberQuery | undefined>;
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly origin!: pulumi.Output<string>;
    public /*out*/ readonly selfLink!: pulumi.Output<string>;
    public readonly serviceAccounts!: pulumi.Output<string[] | undefined>;
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    public readonly userIdsAndEmails!: pulumi.Output<string[] | undefined>;

    /**
     * Create a Group resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: GroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupArgs | GroupState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GroupState | undefined;
            resourceInputs["cplnId"] = state ? state.cplnId : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["identityMatcher"] = state ? state.identityMatcher : undefined;
            resourceInputs["memberQuery"] = state ? state.memberQuery : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["origin"] = state ? state.origin : undefined;
            resourceInputs["selfLink"] = state ? state.selfLink : undefined;
            resourceInputs["serviceAccounts"] = state ? state.serviceAccounts : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
            resourceInputs["userIdsAndEmails"] = state ? state.userIdsAndEmails : undefined;
        } else {
            const args = argsOrState as GroupArgs | undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["identityMatcher"] = args ? args.identityMatcher : undefined;
            resourceInputs["memberQuery"] = args ? args.memberQuery : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["serviceAccounts"] = args ? args.serviceAccounts : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["userIdsAndEmails"] = args ? args.userIdsAndEmails : undefined;
            resourceInputs["cplnId"] = undefined /*out*/;
            resourceInputs["origin"] = undefined /*out*/;
            resourceInputs["selfLink"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Group.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Group resources.
 */
export interface GroupState {
    cplnId?: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    identityMatcher?: pulumi.Input<inputs.GroupIdentityMatcher>;
    memberQuery?: pulumi.Input<inputs.GroupMemberQuery>;
    name?: pulumi.Input<string>;
    origin?: pulumi.Input<string>;
    selfLink?: pulumi.Input<string>;
    serviceAccounts?: pulumi.Input<pulumi.Input<string>[]>;
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    userIdsAndEmails?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a Group resource.
 */
export interface GroupArgs {
    description?: pulumi.Input<string>;
    identityMatcher?: pulumi.Input<inputs.GroupIdentityMatcher>;
    memberQuery?: pulumi.Input<inputs.GroupMemberQuery>;
    name?: pulumi.Input<string>;
    serviceAccounts?: pulumi.Input<pulumi.Input<string>[]>;
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    userIdsAndEmails?: pulumi.Input<pulumi.Input<string>[]>;
}
