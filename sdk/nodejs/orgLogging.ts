// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class OrgLogging extends pulumi.CustomResource {
    /**
     * Get an existing OrgLogging resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrgLoggingState, opts?: pulumi.CustomResourceOptions): OrgLogging {
        return new OrgLogging(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cpln:index/orgLogging:OrgLogging';

    /**
     * Returns true if the given object is an instance of OrgLogging.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OrgLogging {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OrgLogging.__pulumiType;
    }

    public readonly coralogixLoggings!: pulumi.Output<outputs.OrgLoggingCoralogixLogging[] | undefined>;
    public /*out*/ readonly cplnId!: pulumi.Output<string>;
    public readonly datadogLoggings!: pulumi.Output<outputs.OrgLoggingDatadogLogging[] | undefined>;
    public /*out*/ readonly description!: pulumi.Output<string>;
    public readonly elasticLoggings!: pulumi.Output<outputs.OrgLoggingElasticLogging[] | undefined>;
    public readonly logzioLoggings!: pulumi.Output<outputs.OrgLoggingLogzioLogging[] | undefined>;
    public /*out*/ readonly name!: pulumi.Output<string>;
    public readonly s3Loggings!: pulumi.Output<outputs.OrgLoggingS3Logging[] | undefined>;
    public /*out*/ readonly tags!: pulumi.Output<{[key: string]: string}>;

    /**
     * Create a OrgLogging resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: OrgLoggingArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: OrgLoggingArgs | OrgLoggingState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as OrgLoggingState | undefined;
            resourceInputs["coralogixLoggings"] = state ? state.coralogixLoggings : undefined;
            resourceInputs["cplnId"] = state ? state.cplnId : undefined;
            resourceInputs["datadogLoggings"] = state ? state.datadogLoggings : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["elasticLoggings"] = state ? state.elasticLoggings : undefined;
            resourceInputs["logzioLoggings"] = state ? state.logzioLoggings : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["s3Loggings"] = state ? state.s3Loggings : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as OrgLoggingArgs | undefined;
            resourceInputs["coralogixLoggings"] = args ? args.coralogixLoggings : undefined;
            resourceInputs["datadogLoggings"] = args ? args.datadogLoggings : undefined;
            resourceInputs["elasticLoggings"] = args ? args.elasticLoggings : undefined;
            resourceInputs["logzioLoggings"] = args ? args.logzioLoggings : undefined;
            resourceInputs["s3Loggings"] = args ? args.s3Loggings : undefined;
            resourceInputs["cplnId"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(OrgLogging.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering OrgLogging resources.
 */
export interface OrgLoggingState {
    coralogixLoggings?: pulumi.Input<pulumi.Input<inputs.OrgLoggingCoralogixLogging>[]>;
    cplnId?: pulumi.Input<string>;
    datadogLoggings?: pulumi.Input<pulumi.Input<inputs.OrgLoggingDatadogLogging>[]>;
    description?: pulumi.Input<string>;
    elasticLoggings?: pulumi.Input<pulumi.Input<inputs.OrgLoggingElasticLogging>[]>;
    logzioLoggings?: pulumi.Input<pulumi.Input<inputs.OrgLoggingLogzioLogging>[]>;
    name?: pulumi.Input<string>;
    s3Loggings?: pulumi.Input<pulumi.Input<inputs.OrgLoggingS3Logging>[]>;
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a OrgLogging resource.
 */
export interface OrgLoggingArgs {
    coralogixLoggings?: pulumi.Input<pulumi.Input<inputs.OrgLoggingCoralogixLogging>[]>;
    datadogLoggings?: pulumi.Input<pulumi.Input<inputs.OrgLoggingDatadogLogging>[]>;
    elasticLoggings?: pulumi.Input<pulumi.Input<inputs.OrgLoggingElasticLogging>[]>;
    logzioLoggings?: pulumi.Input<pulumi.Input<inputs.OrgLoggingLogzioLogging>[]>;
    s3Loggings?: pulumi.Input<pulumi.Input<inputs.OrgLoggingS3Logging>[]>;
}